package com.example.mello.myapplication;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.ArrayAdapter;
import android.widget.Spinner;

public class GoreserActivity extends AppCompatActivity{
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_select);

        Spinner spinner1 = (Spinner)findViewById(R.id.mySpinner1);
        ArrayAdapter adapter1 = ArrayAdapter.createFromResource(
                this, R.array.univ, android.R.layout.simple_spinner_dropdown_item);
        adapter1.setDropDownViewResource(
                android.R.layout.simple_spinner_dropdown_item);
        spinner1.setAdapter(adapter1);

        Spinner spinner2 = (Spinner)findViewById(R.id.mySpinner2);
        ArrayAdapter adapter2 = ArrayAdapter.createFromResource(
                this, R.array.dept, android.R.layout.simple_spinner_dropdown_item);
        adapter2.setDropDownViewResource(
                android.R.layout.simple_spinner_dropdown_item);
        spinner2.setAdapter(adapter2);

        Spinner spinner3 = (Spinner)findViewById(R.id.mySpinner3);
        ArrayAdapter adapter3 = ArrayAdapter.createFromResource(
                this, R.array.start, android.R.layout.simple_spinner_dropdown_item);
        adapter3.setDropDownViewResource(
                android.R.layout.simple_spinner_dropdown_item);
        spinner3.setAdapter(adapter3);

        Spinner spinner4 = (Spinner)findViewById(R.id.mySpinner4);
        ArrayAdapter adapter4 = ArrayAdapter.createFromResource(
                this, R.array.end, android.R.layout.simple_spinner_dropdown_item);
        adapter4.setDropDownViewResource(
                android.R.layout.simple_spinner_dropdown_item);
        spinner4.setAdapter(adapter4);

    }
}
