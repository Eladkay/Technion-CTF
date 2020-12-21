val fib = mutableListOf(1L, 1L)
fun main() {
    var sum = 0L
    var i = 0
    while(i < 50) {
        sum += fib(i++)
        println(sum)
//        println(fib(i++))
        if(i % 100 == 0) println("current: $sum")
    }
    //println((0..100).first { fibSum(it) > Int.MAX_VALUE })
}
fun fib(n: Int): Long {
    if(fib.size > n) return fib[n]
    val newFib = fib(n-1) + fib(n-2)
    fib.add(newFib)
    return newFib
}
fun fibSum(n: Int): Long {
    return if(n == 0) 0L else fibSum(n-1) + fib(n)
}