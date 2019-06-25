package com.example.appusuario

import android.content.Intent
import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.util.Log
import com.example.appmotorista.R
import kotlinx.android.synthetic.main.activity_cadastro.*
import org.json.JSONObject
import java.net.URL
import java.util.concurrent.Executors

class CadastroActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_cadastro)

        buttonSignIn.setOnClickListener { buttonCadastrarClick() }
    }

    fun getData(){

        val baseUrl = "http://muriloceolin.pythonanywhere.com/"
        val barra = "/"
        val button = buttonSignIn.text
        val username = etUsernameNew.text.toString()
        val senha1 = etSenha1.text.toString()
        val senha2 = etSenha2.text.toString()

        //recupera os valores
        Executors.newSingleThreadExecutor().execute(){
            val json = URL("${baseUrl}${button}${barra}${username}${barra}${senha1}${barra}${senha2}").readText()       //Leio a URL
            val Jsonobj = JSONObject(json)                 // Transformo em um JsonObject
            val resp = listOf(Jsonobj.get("resp"))
            if (resp.get(0).toString() == "Cadastro Realizado com Sucesso")
            {
                VaiPraMain()
                finish()
            }
            else if (resp.get(0).toString() == "*Senhas Diferentes")
            {
                tvResp.text = resp.get(0).toString()
                Log.i("HOLA", resp.get(0).toString() )
            }
        }
    }

    private fun VaiPraMain() {
        startActivity(Intent(this, DestinoActivity::class.java))

    }

    private fun buttonCadastrarClick() {
        getData()
    }
}