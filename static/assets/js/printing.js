let file = document.getElementById("file");
let print_colour = document.getElementById("colour");
let sides = document.getElementById("sides");
let no_of_pages = document.getElementById("no_of_pages").value;
let total_price = document.getElementById("price");
let colour = print_colour.value;
let side = sides.value;
let copies = document.getElementById("copies");
price = 0;

function getPapers() {
    if (sides.value == 2) {
        return Math.floor((no_of_pages + 1) / 2);
    }
    return no_of_pages;
}

function getPrice() {
    if (sides.value == 1 && print_colour.value == 0) {
        return getPapers() * 1.25 * copies.value;
    }
    if (sides.value == 2 && print_colour.value == 0) {
        return getPapers() * 1.5 * copies.value;
    }
    if (sides.value == 1 && print_colour.value == 1) {
        return getPapers() * 10 * copies.value;
    }
}

copies.onchange = function (event) {
    total_price.value = getPrice();
}

print_colour.onchange = function (event) {
    if (print_colour.value == 1) {
        sides.options[1].disabled = true;
    } else {
        sides.options[1].disabled = false;
    }
    total_price.value = getPrice();
}

sides.onchange = function (event) {
    if (sides.value == 2) {
        print_colour.options[1].disabled = true;
    } else {
        print_colour.options[1].disabled = false;
    }
    total_price.value = getPrice();
}

file.onchange = async function (event) {
    var pdf = await event.target.files[0];
    try {
        if (pdf === undefined) {
            document.getElementById("no_of_pages").value = 0;
            total_price.value = 0;
            console.log("no file choosen");
        } else {
            var filereader = new FileReader();
            filereader.onload = async function () {
                var typedarray = new Uint8Array(this.result);
                const task = await pdfjsLib.getDocument(typedarray);
                await task.promise.then((pdf) => {
                    let p = pdf.numPages;
                    document.getElementById("no_of_pages").value = p;
                    no_of_pages = p;
                    total_price.value = getPrice();
                })
            }
            filereader.readAsArrayBuffer(pdf);
        }
    }
    catch(err){
        console.log(err);
    }
}