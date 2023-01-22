let file = document.getElementById("file");
let side =document.getElementById("selectorSideId");
let color = document.getElementById("selectorColorId");
let copies = document.getElementById("copies");
let price = 1.25
let colored = 1
let sides = 1
let pages = 0
let p = 0;
let pr = 1.25;
let n = 1;

console.log("sides",price)
console.log("color",colored)
console.log(file)
function set_price(n){
pages = n;
}

function set_pr(n){
    //console.log(p)
    pr = n;
}

function set_n(a){
    n = a
}
                                            side.onchange = function(event){
                                                sides = event.target.value
                                                
                                                if (sides==2 && colored ==1) {
                                                    p = 1.5;
                                                }else if(sides==1 && colored == 2){
                                                    p = 10;
                                                }
                                                else if(sides==1 && colored == 1){
                                                    p = 1.25;
                                                }
                                                
                                                set_pr(p);
                                                console.log(pr*(pages*n));
                                                document.getElementById("xxx").value = pr*(pages*n);
                                                
                                            }
                                            color.onchange = function(event){
                                                colored = event.target.value
                                                
                                                if (colored == 2){
                                                    document.getElementById("selectorSideId").options[1].disabled=true;
                                                    if (sides == 1){
                                                        p = 10;
                                                    }
                                                }else if(colored == 1){
                                                    document.getElementById("selectorSideId").options[1].disabled=false;
                                                    p = (sides == 2 )? 1.5 : 1.25
                                                }
                                                set_pr(p);
                                                console.log(pr*(pages*n));
                                                document.getElementById("xxx").value = pr*(pages*n);
                                
                                            }
    
                                            copies.onchange = function(event){
                                                n = event.target.value
                                                set_n(n)
                                                console.log(pr)
                                                console.log(pr*(pages*n));
                                                document.getElementById("xxx").value= pr*(pages*n);
                                            }
    
                                            file.onchange =async function (event){
                                                var pdf =await  event.target.files[0]
                                                console.log(pdf)
                                                if (pdf === undefined){
                                                    console.log("no file choosen")
                                                    price = 1.25
                                                    colored = 1
                                                    sides = 1
                                                    pages = 0
                                                    p = 0;
                                                    pr = 1.25;
                                                    n = 1;
                                                    set_price(0)
                                                    console.log(pr*(pages*n));
                                                    document.getElementById("dis-play").value =  pages       
                                                    document.getElementById("xxx").value =  p;
                                                }else{
                                                    var filereader = await new FileReader()
                                                    filereader.onload =async function  (){
                                                        var typedarray =await new Uint8Array(this.result)
                                                        const task = await pdfjsLib.getDocument(typedarray)
                                                        await task.promise.then((pdf)=>{
    
                                                            hi = pdf.numPages
                                                            document.getElementById("dis-play").value =  pdf.numPages      
                                                            console.log(pr*(pages*n));  
                                                            document.getElementById("xxx").value =  pdf.numPages*(pr*n);
                                                            set_price(pdf.numPages)
                                                            
                                                        })
                                                        
                                                    }
                                                
                                                    filereader.readAsArrayBuffer(pdf)  
                                                }
                                            }
                                                         
                                                //console.log(pages)