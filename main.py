from pprint       import pprint

from tools.sorter import Sorter as AlbumSorter

if __name__ == '__main__':
    '''
    This function sorts the user's saved Spotify albums by release date.
    It first gets all saved albums, then sorts them by release date.
    It then removes all saved albums, and resaves them in the sorted order.
    '''
    sorter = AlbumSorter()

    # get all saved albums
    saved_albums = sorter.get_saved_albums()

    # backup
    sorter.backup(saved_albums)

    # check if already sorted
    if sorter.is_sorted(albums=saved_albums, field='date'):
        print('already sorted')
        exit(0)
    else:
        print('not sorted. sorting...')

    # sort by release date
    albums_sorted_by_date = sorter.sort_albums(albums=saved_albums, field='date')

    # remove all
    sorter.remove_albums(albums_sorted_by_date)

    # re-save sorted albums
    sorter.save_albums(albums_sorted_by_date)

    # test if sorted
    if sorter.is_sorted(albums=saved_albums, field='date'):
        print('sorted!')
    else:
        pprint(albums_sorted_by_date)
        raise Exception('not sorted, try again')
