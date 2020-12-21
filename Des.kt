import java.io.File
import java.nio.charset.Charset
import java.util.*
import javax.crypto.Cipher
import javax.crypto.KeyGenerator

val dcipher = Cipher.getInstance("DES")
fun main() {
    //desu
    val keygen = KeyGenerator.getInstance("DES")
    while(true) {
        val key = keygen.generateKey()
        dcipher.init(Cipher.DECRYPT_MODE, key)
        val encrypted = File("ciphertext").readText()
        val dec = decrypt(encrypted)
        if(dec != null)
            println(dec)
    }
}
fun decrypt(str: String): String? {
    try {

        // decode with base64 to get bytes
        val dec: ByteArray = Base64.getDecoder().decode(str.toByteArray())
        val utf8: ByteArray = dcipher.doFinal(dec)

// create new string based on the specified charset
        return String(utf8, Charset.forName("UTF8"))
    } catch (e: Exception) {
    }
    return null
}