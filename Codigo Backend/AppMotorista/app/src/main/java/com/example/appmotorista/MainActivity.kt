package com.example.appmotorista


import android.content.Intent
import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.widget.Toolbar
import kotlinx.android.synthetic.main.activity_login.*
import org.json.JSONObject
import java.net.URL
import java.util.concurrent.Executors

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        buttonLogin.setOnClickListener { buttonLoginClick() }
        buttonCadastrar.setOnClickListener { buttonCadastraClick() }
    }
//
//    //Método para pegar dados da URL com um GET usando apenas Kotlin
    fun getData(){

        val baseUrl = "http://muriloceolin.pythonanywhere.com/"
        val username = etUsername.text.toString()
        val senha = etSenha.text.toString()
        val button = buttonLogin.text.toString()
        val barra = "/"

        Executors.newSingleThreadExecutor().execute{
//            val json = URL("${baseUrl}${complementoUrl}"). readText()
            val json = URL("${baseUrl}${button}${barra}${username}${barra}${senha}"). readText()
            val teste = JSONObject(json)
            val imprimir = listOf(teste.get("resp"))
            if (imprimir.get(0).toString() == "Entrou")
            {
                VaiPraMain()
                finish()
            }
            else
            {
                tvResultado.text = imprimir.get(0).toString()
            };//json;
        }
    }

    private fun VaiPraMain() {
        startActivity(Intent(this, NotificationActivity::class.java))

    }

    fun buttonLoginClick(){
        getData()
    }

    private fun buttonCadastraClick() {
        val username = etUsername.text.toString()
        startActivity(Intent(this, CadastroActivity::class.java).putExtra("username", username))
    }
}

