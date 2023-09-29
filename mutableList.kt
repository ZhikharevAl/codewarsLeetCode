var list: MutableList<Int>? = mutableListOf()

fun main() {
    with(list){
        for (i in 0..<1000) {
            this?.add((Math.random() * 100).toInt())
        }
        println(this?.sum() ?: 0)
        println(this?.max() ?: 0)
        println(this?.min() ?: 0)
        println(this?.average() ?: 0)
        println(this?.first() ?: 0)
        println(this?.last() ?: 0)
        val result = this?.filter {it % 2 == 0} ?: listOf()
        println(result.take(100))
    }
}
