# Carto Print Exporter

Docker-based wrapper around the `carto.print` python library

## Running

## Options

Options can be passed as environment variables

| Option          | Required | Description                                  | Default                                                                       |
| --------------- | -------- | -------------------------------------------- | ----------------------------------------------------------------------------- |
| CARTO_USER_NAME | Yes      | The username of the CARTO map owner          | None                                                                          |
| CARTO_MAP_URL   | Yes      | The ID portion of the Map URL                | None                                                                          |
| CARTO_API_KEY   | No       | The API key used to retrieve the map         | default_public                                                                |
| MAP_WIDTH_CM    | No       | Width of the printable map (in centimeters)  | 100                                                                           |
| MAP_HEIGHT_CM   | No       | Height of the printable map (in centimeters) | 60                                                                            |
| MAP_ZOOM        | No       | Zoom level of the printable map              | 11                                                                            |
| MAP_BBOX        | No       | Bounding box of the printable map            | -73.91754180192949, 40.745569339272336, -73.34899932146074, 40.84979029075523 |
| MAP_DPI         | No       | Resolution of the prinatble map              | 300                                                                           |
| MAP_IMAGE_TYPE  | No       | Image format of the printable map            | CMYK                                                                          |
