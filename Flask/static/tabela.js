$('#resultados').DataTable({});

var d = new Date();            
var strDate = d.getFullYear() + "/" + (d.getMonth()+1) + "/" + d.getDate();
var data_atual = new Date(strDate);

$.get( "http://35.227.122.84:8080/receber_dados_intersystems/1", function( data ) {
    $.each(data.Resultado.Dados.children, function(i, item) {
        var html = "";        
        var date1 = new Date(item.incidentDate);
        var timeDiff = Math.abs(data_atual.getTime() - date1.getTime());
        var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24)); 

        html = html + "<tr>";
        html = html + "<td value='"+item.ID+"'> "+item.ID+"</td>";
        html = html + "<td value='"+item.policyNumber+"'> "+item.policyNumber+"</td>";
        html = html + "<td value='"+item.policyBindDate+"'> "+item.policyBindDate+"</td>";
        html = html + "<td value='"+item.policyState+"'> "+item.policyState+"</td>";
        html = html + "<td value='"+item.incidentType+"'> "+item.incidentType+"</td>";
        html = html + "<td value='"+item.score+"'> "+item.score+"</td>";
        html = html + "<td value='"+item.status+"'> "+item.status+"</td>";
        html = html + "<td value='"+diffDays+"'> "+diffDays+"</td>";
        html = html + "<td><button type=\"button\" id=\"btn_editar_tabela\" style=\"heigth: 10%\" class=\"btn btn-primary\">Edit</button></td>"
        html = html + "<td hidden>" + JSON.stringify(item) + "</td>";
        html = html + "</tr>";
        $('#resultados').DataTable().row.add($(html)).draw();     
    })
});



$('#resultados tbody').on( 'click', 'button', function () {
    var data = $('#resultados').DataTable().row( $(this).parents('tr') ).data();
    var dados_enviar_descricao = data[9];
    var json = JSON.stringify(dados_enviar_descricao); 

    window.location.href = "http://35.227.122.84:8080/description?base64json=" + btoa(json) ;
    $.post( "", function( data ) {
        console.log("Sucesso!");
    });
} );
    





function preenche(dados){    
    console.log(dados);    
}
$("#resultados").on('click','tr',function(e){

    var $row = $(this).closest("tr"),       // Finds the closest row <tr> 
    $tds = $row.find("td");             // Finds all children <td> elements

    var dados = []
    $.each($tds, function() {               // Visits every single <td> element
        dados.push($(this).text());        // Prints out the text within the <td>
    });
    
    //window.location.replace("http://localhost:5000/descricao");

    //preenche(dados);
});

