



 
$(document).ready(function() {
    var table = $('#resultados').DataTable();
     
    $('#filtro_tipo').keyup( function() {
        $.fn.dataTable.ext.search.push(
            function( settings, data, dataIndex ) {
                var tipo = $('#filtro_tipo').val().toLowerCase();
                var type =  data[5].toLowerCase(); // use data for the age column
         
                if (( tipo == type) || ( type.indexOf(tipo) >= 0) && (type.indexOf(tipo) >= 0 ))
                {
                    return true;
                }
                return false;
            }
        );
        table.draw();
    } );

    $('#filtro_valor_max, #filtro_valor_min').keyup( function() {
        $.fn.dataTable.ext.search.push(
            function( settings, data, dataIndex ) {
                var min = parseFloat( $('#filtro_valor_min').val(), 10 );
                var max = parseFloat( $('#filtro_valor_max').val(), 10 );
                var age = parseFloat( data[6] ) || 0; // use data for the age column
         
                if ( ( isNaN( min ) && isNaN( max ) ) ||
                     ( isNaN( min ) && age <= max ) ||
                     ( min <= age   && isNaN( max ) ) ||
                     ( min <= age   && age <= max ) )
                {
                    return true;
                }
                return false;
            }
        );
        table.draw();
    } );

    $('#filtro_score_max, #filtro_score_min').keyup( function() {
        $.fn.dataTable.ext.search.push(
            function( settings, data, dataIndex ) {
                var min = parseFloat( $('#filtro_score_min').val());
                var max = parseFloat( $('#filtro_score_max').val());
                var age = parseFloat( data[7] ) || 0; // use data for the age column
         
                if ( ( isNaN( min ) && isNaN( max ) ) ||
                     ( isNaN( min ) && age <= max ) ||
                     ( min <= age   && isNaN( max ) ) ||
                     ( min <= age   && age <= max ) )
                {
                    return true;
                }
                return false;
            }
        );
        table.draw();
    } );
} );