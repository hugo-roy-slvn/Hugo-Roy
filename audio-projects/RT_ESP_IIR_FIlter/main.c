#include "esp_log.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_timer.h" 

#include "config.h"
#include "i2s_manager.h"
#include "iir_filter.h"
#include "switch_control.h"

extern volatile bool filter_enabled;

static void i2s_loopback_task(void *arg)
{
    i2s_chan_handle_t rx_chan = get_rx_channel();
    i2s_chan_handle_t tx_chan = get_tx_channel();

    int32_t rx_buf[256];
    int16_t tx_buf[256];
    size_t bytes_read, bytes_written;

    for (;;)
    {
        int64_t t_start = esp_timer_get_time();
        if (i2s_channel_read(rx_chan, rx_buf, sizeof(rx_buf), &bytes_read, portMAX_DELAY) == ESP_OK)
        {
            int samples = bytes_read / sizeof(int32_t);

            for (int i = 0; i < samples; i++)
            {
                float x = (float)(rx_buf[i] >> 8) / 8388608.0f;
                float y = filter_enabled ? biquad_process(x) : x;

                if (y > 1.0f) y = 1.0f;
                if (y < -1.0f) y = -1.0f;

                tx_buf[i] = (int16_t)(y * 32767.0f);
            }

            i2s_channel_write(tx_chan, tx_buf, samples * sizeof(int16_t), &bytes_written, pdMS_TO_TICKS(100));
            
            int64_t t_end = esp_timer_get_time();
            int64_t elapsed_us = t_end - t_start;
            ESP_LOGI("LAT", "Bloc traité en %lld us (%.2f ms)", elapsed_us, elapsed_us / 1000.0f);
        }
    }
}

void app_main(void)
{
    ESP_LOGI(TAG, "Starting microphone → amplifier loopback with IIR filter...");

    i2s_init_rx();
    i2s_init_tx();
    biquad_init_default();

    xTaskCreate(i2s_loopback_task, "i2s_loopback_task", 4096, NULL, 10, NULL);
    xTaskCreate(switch_monitor_task, "switch_monitor_task", 2048, NULL, 5, NULL);
}
