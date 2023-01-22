$(document).ready(function(){
    csrf = $("input[name=csrfmiddlewaretoken]").val();
    $(".submit").click(function(){
        var category = $("#category").val();
        var date = $("#date").val();
        $.ajax({
            url:"",
            type:'get',
            data:{
                date:date,
                category:category
            },
            success:function(response){
                $(".table").find("tr:gt(0)").remove();
                txt = ''
                r = response.final
                r.forEach(e => {
                    txt += '<tr id="r-'+e.id+'"><td scope="row">'+e.id+'</td>'
                    txt += '<td scope="row">'+e.date+'</td>'
                    txt += '<td scope="row">'+e.category+'</td>'
                    txt += '<td scope="row">'+e.copies+'</td>'
                    txt += '<td scope="row">'+e.colour+'</td>'
                    txt += '<td scope="row">'+e.sides+'</td>'
                    txt += '<td scope="row"><a href="'+host+url+e.link+'" target="_blank" >Click Here</a></td>'
                    
                    if(e.status == 'Pending'){
                        txt += '<td scope="row" style="color:red;"><strong id="s-'+e.id+'">'+e.status+'</strong></td>'
                        txt += '<td scope="row"><button type="button" class="btn btn-danger" id="'+e.id+'" >Printed</button></td></tr>'
                    }else{
                        txt += '<td scope="row" style="color:green;"><strong id="s-'+e.id+'">'+e.status+'</strong></td></tr>'
                    }
                    
                });
                $(".table").append(txt)
            }
        })
    });
    $(document).on('click',".btn-danger",function(){
        $.ajax({
            url:"",
            type:'post',
            data:{
                id:this.id,
                status:'Printed',
                csrfmiddlewaretoken:csrf
            },
            success:function(response){
                var s_id = '#s-'+response.id
                $(s_id).css('color','green')
                $(s_id).text("Printed")
                $("#"+response.id).remove();
            }
        });
    });
});