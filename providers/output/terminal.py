from __future__ import print_function
import textwrap
from providers.output.provider import OutputProvider

IDENTIFIER = "Terminal"

class Provider(OutputProvider):
    def process_data(self, movie_data):
        movie_data = filter(lambda data: data.get("filmtipset_my_grade_type", "none") != "seen", movie_data)
        movie_data = sorted(movie_data, key=lambda data: data.get("filmtipset_my_grade", 0), reverse=True)
        return movie_data

    def output(self, movie_data):
        movie_data = self.process_data(movie_data)

        print()
        for data in movie_data[:10]:
            print("%s (Filmtipset: %s, IMDB: %s)" % (
                data["title"],
                data["filmtipset_my_grade"] if not data["filmtipset_my_grade"] == 0 else "-",
                data["imdb_rating"],
            ))
            print("  [Genre: %s, Country: %s, Year: %s]" % (
                ", ".join(data["genre"]),
                data["country"],
                data["year"],
            ))
            text = textwrap.wrap('Plot: "' + data["plot"] + '"', width=80, initial_indent="  ", subsequent_indent="  ")
            print("\n".join(text))
            print()
