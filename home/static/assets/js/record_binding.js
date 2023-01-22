let file = document.getElementById("file");
let no_of_pages = document.getElementById("no_of_pages").value;
let total_price = document.getElementById("price");
let copies = document.getElementById("copies");
price = 0;

function getPrice(){
    if (no_of_pages <= 60){
        return 275*copies.value;
    }
    else{
        return (275+(no_of_pages-60)*2)*copies.value;
    }
}



copies.onchange = function(event){
    total_price.value = getPrice();
}

file.onchange =async function (event){
    var pdf =await  event.target.files[0];
    console.log(pdf);
    if (pdf === undefined){
        document.getElementById("no_of_pages").value=0;
        total_price.value = 0;
        console.log("no file choosen");
    }else{
        var filereader = new FileReader();
        filereader.onload =async function  (){
            var typedarray =new Uint8Array(this.result);
            const task = await pdfjsLib.getDocument(typedarray);
            await task.promise.then((pdf)=>{
                let p =  pdf.numPages;
                document.getElementById("no_of_pages").value=p;  
                no_of_pages=p;
                total_price.value = getPrice();;
            })
        }
        filereader.readAsArrayBuffer(pdf);
    }
}