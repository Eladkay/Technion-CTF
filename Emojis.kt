import java.io.File
import java.util.*

fun main() {
//    val emojis = "📽🎱🤖🐲👶🤖🤘👶🤖🌺😃🤘🆕✨😎🆕🕹💪🤖🆕🤘🐲👶🤘🐲🤘🐵🤖👶📽👏🌺👶🤖👶🤖🌺😃🤘🐵✨👶😪🚩🍝🤘📽🎱😞👀🤘🍕😎🐲🌺🐂👶👶🤖🌺😃🤘🍕😎💪👶🤘🕹🐲✨🐂🤘🍕👏🤘👿🤖🤘🍕😃👿🙂🐵🙂😎🤖🚩👀🤘✨🐲🌺🤘🚩👏🆕🤘👶🤖🌺😃🤘👿🤖🤘🍃🤖🐂🐲👶🐲🍕🕹💪🤘📽🎱🤖🐲👶🤖🤖🌺🍕🤖🐵🤘🐂🐂✨👿📽😎🕹🎵🤘🐲🌺😃🤘👶🤖🌺😃🤘💪🍕🚩👏👀🤘👶🤖🌺😃🤘🐂🍕😞🆕👏🚩😎🍝🍝🐂🆕🎱👶🤖🌺😃🤘😃🍃🖐✨🐂🐲🆕😞👿🤘📽🎱😞👀🤘🍕😎🐲🌺🐂👶📽🎱🤖🐲👶🤖🤘👶🤖🌺😃🤘🆕✨😎🆕🕹💪🤖🆕🤘🐲👶🤘🐲🤘🐵🤖👶📽👏🌺👶🤖👶🤖🌺😃🤘🐵✨👶😪🚩🍝🤘📽🎱😞👀🤘🍕😎🐲🌺🐂👶👶🤖🌺😃🤘🍕😎💪👶🤘🕹🐲✨🐂🤘🍕👏🤘👿🤖🤘🍕😃👿🙂🐵🙂😎🤖🚩👀🤘✨🐲🌺🤘🚩👏🆕🤘👶🤖🌺😃🤘👿🤖🤘🍃🤖🐂🐲👶🐲🍕🕹💪🤘📽🎱🤖🐲👶🤖🤖🌺🍕🤖🐵🤘🐂🐂✨👿📽😎🕹🎵🤘🐲🌺😃🤘👶🤖🌺😃🤘💪🍕🚩👏👀🤘👶🤖🌺😃🤘🐂🍕😞🆕👏🚩😎🍝🍝🐂🆕🎱👶🤖🌺😃🤘😃🍃🖐✨🐂🐲🆕😞👿🤘📽🎱😞👀🤘🍕😎🐲🌺🐂👶"//"📷😋🤘📽🎱🤖🐲👶🤖🤘👶🤖🌺😃🤘🆕✨😎🆕🕹💪🤖🆕🤘🐲👶🤘🐲🤘🐵🤖👶📽👏🌺👶🤖📷😋🤘👶🤖🌺😃🤘🐵✨👶😪🚩🍝🤘📽🎱😞👀🤘🍕😎🐲🌺🐂👶📷😋🤘👶🤖🌺😃🤘🍕😎💪👶🤘🕹🐲✨🐂🤘🍕👏🤘👿🤖🤘🍕😃👿🙂🐵🙂📷😋🤘😎🤖🚩👀🤘✨🐲🌺🤘🚩👏🆕🤘👶🤖🌺😃🤘👿🤖🤘🍃🤖🐂🐲👶🐲🍕🕹💪🤘📽🎱🤖🐲👶🤖📷😋🤘🤖🌺🍕🤖🐵🤘🐂🐂✨👿📽😎🕹🎵🤘🐲🌺😃🤘👶🤖🌺😃🤘💪🍕📷😋🤘🚩👏👀🤘👶🤖🌺😃🤘🐂🍕😞🆕👏🚩😎🍝🍝🐂🆕🎱📷😋🤘👶🤖🌺😃🤘😃🍃🖐✨🐂🐲🆕😞👿🤘📽🎱😞👀🤘🍕😎🐲🌺🐂👶"
//    val letters = " et.aoinshrdlcumwfgypbvkjxqz"
//    val freq = emojis.toList().distinct().map { it to Collections.frequency(emojis.toList(), it) }.sortedBy { it.second }.reversed()
//    val map = letters.mapIndexed { index, c -> freq[index].first to c }
//    println(map)
//    println(map.first { it.first.toString() == "🤘" })
//    val toTranslate = "📷😋🤘📽🎱🤖🐲👶🤖🤘👶🤖🌺😃🤘🆕✨😎🆕🕹💪🤖🆕🤘🐲👶🤘🐲🤘🐵🤖👶📽👏🌺👶🤖"//"🍕😎🐲🍕👶🤘🌺👏🍕🤘💪🍕🤘✨😎💪🤖🎵"
//    println(toTranslate.map { it1->map.firstOrNull { it.first == it1 }?.second }.joinToString(""))
    val file = File("english-word-list-total.csv")
    val read = file.readLines().filter { !it.startsWith(";") }.map { it.split(";")[1] }.joinToString("\n")
    val newFile = File("words_by_freq_old")
    newFile.createNewFile()
    newFile.writeText(read)

}

