import scrapy


class RegionDataSpider(scrapy.Spider):
    name = "region_data"
    allowed_domains = ["nadezhdin2024.ru"]
    start_urls = ["https://nadezhdin2024.ru/addresses"]

    @staticmethod
    def get_progress(progress_text):
        if not progress_text:
            return None

        words = progress_text.split()
        numbers = []
        for word in words:
            if word.isdigit():
                numbers.append(int(word))

        if 2500 in numbers:
            numbers.remove(2500)

        if len(numbers) == 0:
            print(f"Error: no numbers in progress text: {progress_text}")
            return None

        if len(numbers) != 1:
            print(f"Error: more than one number in progress text: {progress_text}")
            return None

        return numbers[0]

    def parse(self, response):
        for region in response.css('div.addresses-page__region'):
            region_name = region.css("h3.subheading::text").get()

            progress_text = region.css("span.progressbar__el__text::text").get()
            progress = self.get_progress(progress_text)
            if progress is None:
                continue

            yield {
                "region_name": region_name,
                "progress": progress,
            }
