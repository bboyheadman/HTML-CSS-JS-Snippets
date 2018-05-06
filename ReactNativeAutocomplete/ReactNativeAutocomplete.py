import sublime
import sublime_plugin


def load_autocompletes(key):
	res = []
	try:
		res = sublime.decode_value(
			sublime.load_resource("Packages/User/Completions/%s.reactnative-autocomplete" % key)
		)["completions"]
	except:
		pass
	return res


class ReactNativeAutocomplete(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		sn = view.scope_name(locations[0]).split(" ")[0]
		if sn not in ["source.jsx"]:
			return None

		curr_pos = view.sel()[0].begin()
		current_obj_region = view.word(curr_pos - 1)
		current_obj = view.substr(current_obj_region)

		return load_autocompletes(current_obj)
