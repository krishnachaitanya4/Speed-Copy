$(document).ready(function(){
    csrf = $("input[name=csrfmiddlewaretoken]").val();
    $(".submit").click(function(){
        var status = $("#status").val();
        var date = $("#date").val();
        $.ajax({
            url:"",
            type:'get',
            data:{
                date:date,
                status:status
            },
            success:function(response){
                $(".table").find("tr:gt(0)").remove();
                txt = ''
                r = response.orders
                r.forEach(e => {
                    txt += '<tr id="r-'+e.id+'"><td scope="row">'+e.id+'</td>'
                    txt += '<td scope="row">'+e.customer_id+'</td>'
                    txt += '<td scope="row">'+e.date+'</td>'
                    txt += '<td scope="row">'+e.price+'</td>'
                    txt += '<td scope="row">'+e.college+'</td>'
            
                    
                    if (e.status == "Order Received"){
                        txt += '<td><select class="form-select" id="s-'+e.id+'" aria-label="Default select example">'
                        txt += '<option value="Order Received" selected>Order Received</option>'
                        txt += '<option value="Printed">Printed</option>'
                        txt += '<option value="Shipped">Shipped</option>'
                        txt += '<option value="Delivered">Delivered</option></td>'
                        txt += '<td><button type="button" id="'+e.id+'" class="btn btn-outline-danger">Update</button></td>'
                    }else if (e.status == "Printed"){
                        txt += '<td><select class="form-select" id="s-'+e.id+'" aria-label="Default select example">'
                        txt += '<option value="Order Received">Order Received</option>'
                        txt += '<option value="Printed" selected>Printed</option>'
                        txt += '<option value="Shipped">Shipped</option>'
                        txt += '<option value="Delivered">Delivered</option></td>'
                        txt += '<td><button type="button" id="'+e.id+'" class="btn btn-outline-danger">Update</button></td>'

                    }else if (e.status == "Shipped"){
                        txt += '<td><select class="form-select" id="s-'+e.id+'" aria-label="Default select example">'
                        txt += '<option value="Order Received">Order Received</option>'
                        txt +='<option value="Printed">Printed</option>'
                        txt += '<option value="Shipped"  selected>Shipped</option>'
                        txt += '<option value="Delivered">Delivered</option></td>'
                        txt += '<td><button type="button" id="'+e.id+'" class="btn btn-outline-danger">Update</button></td>'

                    }else{
                        txt += '<td><strong style="color:green">Delivered</strong></td>'
                    }

                    txt += '</tr>'
                });
                $(".table").append(txt)
            }
        })
    });
    $(document).on('click',".btn-outline-danger",function(){
        var s_id = '#s-'+this.id;
        var status = $(s_id).val();
        
        $.ajax({
            url:"",
            type:'post',
            data:{
                id:this.id,
                status:status,
                csrfmiddlewaretoken:csrf
            },
            success:function(response){
                var s_id = '#s-'+response.id
                if (response.status == "Delivered"){
                    $(s_id).replaceWith('<strong style="color:green">Delivered</strong>');
                    $('#'+response.id).remove();
                }
            }
        });
    });
}); 