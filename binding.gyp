{
  "targets": [
    {
      "target_name": "hello",
      "sources": [ "binding.cpp" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}
