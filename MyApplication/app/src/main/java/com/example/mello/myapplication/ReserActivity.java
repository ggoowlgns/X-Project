package com.example.mello.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

public class ReserActivity extends AppCompatActivity {
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_reser);

        Button button1 = (Button) findViewById(R.id.book);
        button1.setOnClickListener(new View.OnClickListener()
        {
            public void onClick(View v)
            {
                Intent intent = new Intent(ReserActivity.this, RelistActivity.class);
                startActivity(intent);
            }
        });

        Button button2 = (Button) findViewById(R.id.note);
        button2.setOnClickListener(new View.OnClickListener()
        {
            public void onClick(View v)
            {
                Intent intent = new Intent(ReserActivity.this, GoreserActivity.class);
                startActivity(intent);
            }
        });

        Button button3 = (Button) findViewById(R.id.rule);
        button3.setOnClickListener(new View.OnClickListener()
        {
            public void onClick(View v)
            {
                Intent intent = new Intent(ReserActivity.this, RuleActivity.class);
                startActivity(intent);
            }
        });

        Button button4 = (Button) findViewById(R.id.rule);
        button4.setOnClickListener(new View.OnClickListener()
        {
            public void onClick(View v)
            {
                Intent intent = new Intent(ReserActivity.this, HowActivity.class);
                startActivity(intent);
            }
        });
    }
}
