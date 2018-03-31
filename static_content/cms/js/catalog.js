jQuery(function ($) {

    $('.dd').nestable();

    $('.dd-handle a').on('mousedown', function (e) {
        e.stopPropagation();
    });

    $('[data-rel="tooltip"]').tooltip();

});

function createModal(title, url) {
    var dialog = bootbox.dialog({
        title: title,
        message: '<p><i class="fa fa-spin fa-spinner"></i> Loading...</p>'
    });
    dialog.init(function () {
        setTimeout(function () {
            dialog.find('.bootbox-body').html(getContent(url));
        }, 3000);
    });
}

function editCatalogItem(e) {
    createModal('Редактировать Категорию', 's');
}

function addSubCatalogItem(e) {
    createModal('Добавить подкатегорию', 's')
}
function getContent(url) {
    return 'I was loaded after the dialog was shown!';
}