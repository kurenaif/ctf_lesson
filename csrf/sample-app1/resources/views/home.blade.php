<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="csrf-token" content="{{ csrf_token() }}">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <style>
        body {
            margin: 10px;
        }
    </style>

    <title>{{ config('app.name', 'Laravel') }}</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&display=swap">
</head>

<body>
    <form class="form-inline">
        <div class="row g-1">
            <div class="col-auto form-group">
                <input type="text" class="form-control" placeholder="パスワード" id="pw">
            </div>
            <button type="submit" class="col-auto btn btn-primary">post</button>
        </div>
    </form>

        <div class="row g-1">
            <div class="col-auto">user_name</div>
            <div class="col-auto">content</div>
        </div>
        <div class="row g-1">
            <div class="col-auto">user_name</div>
            <div class="col-auto">content</div>
        </div>
        <div class="row g-1">
            <div class="col-auto">user_name</div>
            <div class="col-auto">content</div>
        </div>
        <div class="row g-1">
            <div class="col-auto">user_name</div>
            <div class="col-auto">content</div>
        </div>
</body>

</html>