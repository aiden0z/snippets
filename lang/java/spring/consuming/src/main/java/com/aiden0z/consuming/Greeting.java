package com.aiden0z.consuming;


import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;

@JsonIgnoreProperties(ignoreUnknown = true)
@Data
public class Greeting {
    private long id;
    private String content;
}

