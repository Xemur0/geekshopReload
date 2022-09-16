window.onload = function () {
    $(document).on('click', '.category_delete', function () {

        let t_href = event.target;
        var csrf = $('meta[name="csrf-token"]').attr('content');
        console.log(t_href.value);
        console.log(csrf);
        $.ajax({
            type: 'DELETE',
            headers: {"X-CSRFToken": csrf},
            url: '/admins/category-delete/' + t_href.value + '/',
            success: function (data) {
                $('.delete_category').html(data.result)
                $('#dataTable').DataTable();
            },
        });
        Event.preventDefault();
    })

}