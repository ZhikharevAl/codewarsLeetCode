fun getFilename(path: String): String {
    val parts = path.split("/")
    val filenameWithExtension = parts.last()
    val filenameParts = filenameWithExtension.split(".")
    return filenameParts.first()
}
