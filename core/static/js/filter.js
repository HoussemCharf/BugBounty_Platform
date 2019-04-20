$(document).ready(function() {
    $('#btnPending').click(function() {
        $("#myTable tr td").each(function() {
            var cell = $(this).text();
            if ($.trim(cell) == 'Pending' ||$.trim(cell) == 'Rejected' ) {
                $(this).parent().hide();
            }
        });
    });
    $('#btnAccepted').click(function() {
        $("#myTable tr td").each(function() {
            var cell = $(this).text();
            if ($.trim(cell) == 'Accepted' || $.trim(cell) == 'Rejected') {
                $(this).parent().hide();
            }
        });
    });
    $('#btnRejected').click(function() {
        $("#myTable tr td").each(function() {
            var cell = $(this).text();
            if ($.trim(cell) == 'Accepted' || $.trim(cell)== 'Pending') {
                $(this).parent().hide();
            }
        });
    });
     $('#btnReset').click(function() {
        $("#myTable tr").each(function() {
            $(this).show();
        });
    });
});