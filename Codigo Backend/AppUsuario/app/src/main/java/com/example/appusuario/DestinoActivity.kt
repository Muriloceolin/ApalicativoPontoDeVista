package com.example.appusuario

import android.content.Intent
import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import com.example.appmotorista.R
import kotlinx.android.synthetic.main.activity_notification.*

class DestinoActivity : AppCompatActivity(){
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_notification)

        buttonIniciaRota.setOnClickListener { buttonIniciaRotaClick() }

    }


    private fun buttonIniciaRotaClick() {
        startActivity(Intent(this, RotaIniciada::class.java))
    }
}