package com.example.mello.myapplication;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

public class SubActivity extends AppCompatActivity {

    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sub);

        Intent intent = getIntent();
        String data = intent.getStringExtra("value");

        Button button = (Button) findViewById(R.id.btn_study);
        button.setOnClickListener(new android.view.View.OnClickListener()
        {
            public void onClick(View v)
            {
                Intent intent = new Intent(SubActivity.this, ReserActivity.class);
                startActivity(intent);
            }
        });
    }
}
