let file = document.getElementById("file");
let print_colour = document.getElementById("colour");
let sides = document.getElementById("sides");
let no_of_pages = document.getElementById("no_of_pages").value;
let total_price = document.getElementById("price");
let colour = print_colour.value;
let side = sides.value;
let copies = document.getElementById("copies");
let ele = document.getElementById("p_colour")
let colour_pages = document.getElementById("colour_pages")
price = 0;

colour_pages.onchange = function (event) {
    console.log(event.target.value)
}

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

print_colour.onchange = function (event) {
    if (print_colour.value == 1) {
        sides.options[1].disabled = true;
        ele.style.display = "none";
        colour_pages.required = false;
    } else if (print_colour.value == 0) {
        sides.options[1].disabled = false;
        ele.style.display = "none";
        colour_pages.required = false;
    } else if (print_colour.value == 2) {
        console.log('selected');
        ele.style.display = "";
        colour_pages.required = true;

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
    catch (err) {
        console.log(err);
    }
}
function validate(s) {
    for (i = 0; i < s.length; i++) {
        aasci = s[i].charCodeAt()
        if ((aasci <= 57 && aasci >= 48) || aasci == 44 || aasci == 45);
        else {
            return false;
        }
        if(i<s.length-1){
            if ((s[i] == ',' && s[i+1] == ',')||(s[i]==',' && s[i+1] == '-')
            ||(s[i]=='-' && s[i+1] == ',')||(s[i]=='-' && s[i+1] == '-')){
                return false;
            }
        }
    }
    return true;
}
function removeDuplicates(arr) {
    return arr.filter((item, 
        index) => arr.indexOf(item) === index);
}
customInput = function (event) {
    str = event.target.value
    if (validate(str)) {
        if (str[str.length-1]==',' || str[str.length-1] == '-'){
            str = str.slice(0,str.length-1)
        }
        const l = str.split(",")
        console.log(l)
        const final_list = []
        for (i = 0;i<l.length;i++){
            var num = Number(l[i]);
            console.log(num,l[i],typeof l[i])
            if (isNaN(num)){
                const l2 = l[i].split("-")
                n1 = Number(l2[0])
                n2 = Number(l2[1])
                if (n1>n2){
                    n2 = n1+n2;
                    n1 = n2-n1;
                    n2 = n2-n1;
                }
                for (j = n1;j<=n2;j++){
                    final_list.push(j)
                }
            }else{
                final_list.push(num)
            }
        }
        final = removeDuplicates(final_list)
        console.log(final)
        if (no_of_pages!=0){
            let p = final.length * 10 + ((no_of_pages * 1.25) - (final.length * 1.25))
            total_price.value = p;
        }
    }else{
        this.value = str.slice(0,str.length-1);
        window.alert("only numbers,commas and hiphens are accepted.");
    }
}
colour_pages.addEventListener("input", customInput)