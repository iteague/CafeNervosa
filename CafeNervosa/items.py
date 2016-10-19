import scrapy


class SeasonItems(scrapy.Item):
	SeasonNumber = scrapy.Field()
	EpisodeList = scrapy.Field()
