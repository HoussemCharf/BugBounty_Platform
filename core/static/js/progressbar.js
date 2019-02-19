function update_progressbar() {
    var opt1 = parseInt( $('option:selected', $('#selectA')).val() );
    var total = isNaN( opt1 ) ? 0 : opt1;
    $("#progressBar").prop( 'value', total )
}
$('#selectA').on( 'change', update_progressbar );
