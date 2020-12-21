
import java.awt.image.DataBufferByte
import java.io.File
import java.util.*
import javax.imageio.ImageIO


fun main() {
    val set = mutableListOf<ByteArray>()
    for(i in 0 until 100000) {
        val img = ImageIO.read(File("C:\\Users\\Elad\\Downloads\\ctf\\NandScript\\frame$i.jpg"))
        val pixels = (img.raster.dataBuffer as DataBufferByte).data
        if(set.none { Arrays.equals(it, pixels) }) {
            println(i)
            set.add(pixels)
        }

    }
}