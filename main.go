package main

import (
	"github.com/shunyeka-spl/steampipe-plugin-abaiazure/abaiazure"
	"github.com/turbot/steampipe-plugin-sdk/v4/plugin"
)

func main() {
	plugin.Serve(&plugin.ServeOpts{PluginFunc: abaiazure.Plugin})
}
