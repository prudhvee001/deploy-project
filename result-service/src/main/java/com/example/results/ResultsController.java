package com.example.results;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
public class ResultsServiceApplication {

    public static void main(String[] args) {
        SpringApplication.run(ResultsServiceApplication.class, args);
    }

    @RestController
    class ResultsController {
        @GetMapping("/results")
        public String getResults() {
            return "{\"subject\": \"Math\", \"score\": \"85%\"}";
        }
    }
}
