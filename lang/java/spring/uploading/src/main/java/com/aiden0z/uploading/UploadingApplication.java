package com.aiden0z.uploading;

import com.aiden0z.uploading.storage.StorageProperties;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.EnableConfigurationProperties;

@SpringBootApplication
@EnableConfigurationProperties(StorageProperties.class)
public class UploadingApplication {

    public static void main(String[] args) {
        SpringApplication.run(UploadingApplication.class, args);
    }

}
