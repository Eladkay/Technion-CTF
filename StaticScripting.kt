import java.awt.Image
import java.awt.image.BufferedImage
import java.awt.image.DataBufferByte
import java.io.File
import javax.imageio.ImageIO

fun main() {
    val newImage = BufferedImage(160, 90, BufferedImage.TYPE_INT_RGB)
    for (k in 0 until 14400) {
        val i = k % 160
        val j = k / 160
        val img = ImageIO.read(File("C:\\Users\\Elad\\Downloads\\ctf\\static\\frame$k.jpg"))
        newImage.setRGB(i, j, img.getRGB(i, j))
    }
    ImageIO.write(newImage, "jpg", File("out.jpg"))
}