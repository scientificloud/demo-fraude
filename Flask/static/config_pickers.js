var meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
]
var meses_abreviado = [
    'Jan',
    'Fev',
    'Mar',
    'Abr',
    'Mai',
    'Jun',
    'Jul',
    'Ago',
    'Set',
    'Out',
    'Nov',
    'Dez'
]
var semana = [
    'Dom',
    'Seg',
    'Ter',
    'Qua',
    'Qui',
    'Sex',
    'Sab'
]
var linguagem = {
    months: meses,
    weekdaysShort: semana,
    monthsShort: meses_abreviado,
    weekdaysAbbrev:	['D','S','T','Q','Q','S','S']
}

document.addEventListener('DOMContentLoaded', function() {
    var options = {
        format: 'dd mmmm yy',
        i18n: linguagem
    }
    var elems = document.querySelectorAll('.datepicker');
    var instances = M.Datepicker.init(elems, options);
}); 

document.addEventListener('DOMContentLoaded', function() {
    var options = {
        i18n:{
            cancel: "Cancelar",
            clear: "Limpar",
            done: "Ok"
        },
        defaultTime: 'now',
        twelveHour: false
    }
    var elems = document.querySelectorAll('.timepicker');
    var instances = M.Timepicker.init(elems, options);
});