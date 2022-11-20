package main

import (
	"github.com/shunyeka-spl/steampipe-plugin-abaiazure/abaiazure"
	"github.com/turbot/steampipe-plugin-sdk/plugin"
)

func main() {
	plugin.Serve(&plugin.ServeOpts{PluginFunc: abaiazure.Plugin})
}
