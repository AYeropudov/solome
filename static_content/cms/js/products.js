jQuery(function ($) {

    /////////////////////////////////
    //table checkboxes
    $('th input[type=checkbox], td input[type=checkbox]').prop('checked', false);

    //And for the first simple table, which doesn't have TableTools or dataTables
    //select/deselect all rows according to table header checkbox
    var active_class = 'active';
    $('#simple-table > thead > tr > th input[type=checkbox]').eq(0).on('click', function () {
        var th_checked = this.checked;//checkbox inside "TH" table header

        $(this).closest('table').find('tbody > tr').each(function () {
            var row = this;
            if (th_checked) $(row).addClass(active_class).find('input[type=checkbox]').eq(0).prop('checked', true);
            else $(row).removeClass(active_class).find('input[type=checkbox]').eq(0).prop('checked', false);
        });
    });

    //select/deselect a row when the checkbox is checked/unchecked
    $('#simple-table').on('click', 'td input[type=checkbox]', function () {
        var $row = $(this).closest('tr');
        if ($row.is('.detail-row ')) return;
        if (this.checked) $row.addClass(active_class);
        else $row.removeClass(active_class);
    });


    /********************************/
    //add tooltip for small view action buttons in dropdown menu
    $('[data-rel="tooltip"]').tooltip({placement: tooltip_placement});

    //tooltip placement on right or left
    function tooltip_placement(context, source) {
        var $source = $(source);
        var $parent = $source.closest('table')
        var off1 = $parent.offset();
        var w1 = $parent.width();

        var off2 = $source.offset();
        //var w2 = $source.width();

        if (parseInt(off2.left) < parseInt(off1.left) + parseInt(w1 / 2)) return 'right';
        return 'left';
    }


    /***************/
    $('.show-details-btn').on('click', function (e) {
        e.preventDefault();
        $(this).closest('tr').next().toggleClass('open');
        $(this).find(ace.vars['.icon']).toggleClass('fa-angle-double-down').toggleClass('fa-angle-double-up');
    });
    /***************/


    /**
     //add horizontal scrollbars to a simple table
     $('#simple-table').css({'width':'2000px', 'max-width': 'none'}).wrap('<div style="width: 1000px;" />').parent().ace_scroll(
     {
       horizontal: true,
       styleClass: 'scroll-top scroll-dark scroll-visible',//show the scrollbars on top(default is bottom)
       size: 2000,
       mouseWheelLock: true
     }
     ).css('padding-top', '12px');
     */
    
    $('.copy-product').on('click', function (e) {
        let _target = $(e.currentTarget);
        let product_id = _target.data('id');
        $.ajax({
            method: 'POST',
            dataType: 'json',
            data: {},
            processData: false,
            contentType: false,
            beforeSend: function(xhr) {xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());},
            url: '/cms/products/copy/'+product_id
        })
            .done(function (msg) {
               window.location = msg.location;
            })
            .error(function (msg) {
                console.log(msg);
            });
    });

    $('.tagging').on('click', function () {
       let _products = $('.mass-product:checked');
       let _dualList = null;

       let putTags = function () {
         try {
             $.ajax({
            method: 'POST',
            dataType: 'json',
            data: {"products": data},
            processData: false,
            contentType: false,
            beforeSend: function(xhr) {xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());},
            url: '/cms/products/copy/'+product_id
            })
            .done(function (msg) {
               window.location = msg.location;
            })
            .error(function (msg) {
                console.log(msg);
            });
             console.log(_dualList.val());
         } catch (e) {
         }
       };

       let data = [];
        _products.each(function (index) {
           data.push(_products[index].value);
       });
        let _dialog =bootbox.dialog({
            title: "Массовое присвоение тегов",
            message: '<p><i class="fa fa-spin fa-spinner"></i> Loading...</p>',
            size: 'large',
            buttons: {
                confirm: {
                    label: 'Your button text',
                    className: "some-class",
                    callback: putTags
                }
            }
        });

        _dialog.init(function () {
            $.get('/cms/modals/tags/tagging', function (data) {
                _dialog.find('.bootbox-body').html(data);
                _dualList = $('select[name="tags[]"]').bootstrapDualListbox(
                    {
                        infoText:"Доступно {0}",
                        infoTextEmpty: "Доступно 0",
                        infoTextFiltered: '<span class="label label-purple label-lg">Отфильтрованные</span>',
                        nonSelectedListLabel: 'Доступные',
                        selectedListLabel: 'Выбранные',
                    }
                );
                let container1 = _dualList.bootstrapDualListbox('getContainer');
                container1.find('.btn').addClass('btn-white btn-info btn-bold');
            }, _dualList)
        }, _dualList)
        // var demo1 = $('select[name="duallistbox_demo1[]"]').bootstrapDualListbox({infoTextFiltered: '<span class="label label-purple label-lg">Filtered</span>'});
        // var container1 = demo1.bootstrapDualListbox('getContainer');
        // container1.find('.btn').addClass('btn-white btn-info btn-bold');

        // $.ajax({
        //     method: 'POST',
        //     dataType: 'json',
        //     data: {"products": data},
        //     processData: false,
        //     contentType: false,
        //     beforeSend: function(xhr) {xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());},
        //     url: '/cms/products/copy/'+product_id
        // })
        //     .done(function (msg) {
        //        window.location = msg.location;
        //     })
        //     .error(function (msg) {
        //         console.log(msg);
        //     });
    });

});

