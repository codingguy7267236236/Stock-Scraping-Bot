import nextcord

#function to create an embed for dscord
#title is the title of embed
#description is the description it has
#values represented in a list of lists ([["Price",200],["Price",150]]) of the values to add to embed
#thumbnail represents the url to use as the thumbnail
def createEmbed(title,description,values,thumbnail=None):
    embed = nextcord.Embed(title=title,description=description)
    #checking is any values have been passed
    for i in values:
        name = i[0]
        value = i[1]
        #adding fields to embed
        embed.add_field(name=name,value=value)
    #checking if a thumbnail has been specified
    if thumbnail != None:
        embed.set_thumbnail(url=thumbnail)
    
    #returning the embed once it has been constructed
    return embed