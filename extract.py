# Extract jpg's from pdf's. Quick and dirty.
name = "book.pdf"

with open(name, "rb") as f:
    pdf = f.read()

start_mark = b"\xff\xd8"
start_fix = 0
end_mark = b"\xff\xd9"
end_fix = 2
i = 0

n_jpg = 0
while True:
    if n_jpg > 0:
        break
    i_stream = pdf.find(b"stream", i)
    if i_stream < 0:
        break
    i_start = pdf.find(start_mark, i_stream, i_stream + 20)
    if i_start < 0:
        i = i_stream + 20
        continue
    i_end = pdf.find(b"endstream", i_start)
    if i_end < 0:
        raise Exception("Didn't find end of stream!")
    i_end = pdf.find(end_mark, i_end - 20)
    if i_end < 0:
        raise Exception("Didn't find end of JPG!")

    i_start += start_fix
    i_end += end_fix
    print(f"JPG {n_jpg} from {i_start} to {i_end}")
    jpg = pdf[i_start:i_end]

    with open(f"out/{n_jpg}.jpg", "wb") as jpg_file:
        jpg_file.write(jpg)

    n_jpg += 1
    i = i_end
