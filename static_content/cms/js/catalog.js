var catalogObject = function () {
    this.dialog = null;
    this.init = function () {
        this.nestListInit();
        var _this = this;
        $(".edit-cat-btn").bind("click", function (e) {
            _this.editCatalogItem(e);
        });
        $(".add-subcat-btn").bind("click", function (e) {
            _this.addSubCatalogItem(e);
        });
    };

    this.nestListInit = function () {
        jQuery(function ($) {

            $('.dd').nestable();

            $('.dd-handle a').on('mousedown', function (e) {
                e.stopPropagation();
            });

            $('[data-rel="tooltip"]').tooltip();

        });
    };

    this.createModal = function (title, typeModal, data) {
        var _this = this;
        _this.dialog = bootbox.dialog({
            title: title,
            message: '<p><i class="fa fa-spin fa-spinner"></i> Loading...</p>'
        });

        _this.dialog.init(function (){
            _this.doRequest(
                '/cms/catalog/m/' + typeModal,
                data,
                {method:"GET", dataType:"html"},
                function (result) {
                    _this.dialog.find('.bootbox-body').html(result);
                }
                );
        });
    };

    this.editCatalogItem = function (e) {
        var target = $(e.currentTarget);
        this.createModal('Редактировать Категорию', 'editCat', {catId:target.data("id")});
    };

    this.addSubCatalogItem = function (e) {
        var target = $(e.currentTarget);
        this.createModal('Добавить подкатегорию', 'createSubCat', {catId:target.data("id")})
    };

    this.getContent = function (url) {
        return 'I was loaded after the dialog was shown!';
    };

    this.doRequest = function (url, data, options, someCall) {
        var result = '';
        var _this = this;
        $.ajax({
            method: options.method,
            dataType: options.dataType,
            data: data,
            url: url
        })
            .done(function (msg) {
               someCall(msg);
            })
            .error(function (msg) {
                someCall(msg);
            });
    }
};

function submitForm(e) {
    var button = $(e);
    var form = $("#"+ button.data("form"));
    var data = form.serializeArray();
    $.ajax({
            method: form.data("method"),
            dataType: 'json',
            data: data,
            url: form.data("action")
        })
            .done(function (msg) {
               console.log(msg);
            })
            .error(function (msg) {
                console.log(msg);
            });
}

var catalogApplication = new catalogObject();
catalogApplication.init();






