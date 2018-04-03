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
        $(".add-root").bind("click", function (e) {
            _this.addRoot(e);
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
            var whitelist_ext = ["jpeg", "jpg", "png", "gif" , "bmp"];
            var whitelist_mime = ["image/jpg", "image/jpeg", "image/png", "image/gif", "image/bmp"];
            _this.doRequest(
                '/cms/catalog/m/' + typeModal,
                data,
                {method:"GET", dataType:"html"},
                function (result) {
                    _this.dialog.find('.bootbox-body').html(result);
                    $('input[type=file]').ace_file_input({
					style:'well',
					btn_choose:'Drop files here or click to choose',
					btn_change:null,
					no_icon:'ace-icon fa fa-cloud-upload',
					droppable:true,
					thumbnail:'large',
                    allowExt: whitelist_ext,
                    allowMime: whitelist_mime
				})
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

    this.addRoot = function (e) {
        var target = $(e.currentTarget);
        this.createModal('Добавить категорию', 'createRoot', {})
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
    var data = new FormData(form[0]);
    $.ajax({
            method: form.data("method"),
            dataType: 'json',
            data: data,
            processData: false,
            contentType: false,
            beforeSend: function(xhr) {xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());},
            url: form.data("action")
        })
            .done(function (msg) {
               catalogApplication.dialog.modal('hide');
               window.location.reload();
            })
            .error(function (msg) {
                console.log(msg);
            });
}

var catalogApplication = new catalogObject();
catalogApplication.init();






