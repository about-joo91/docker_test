from utils import get_movie_info


def test_get_movie_info():
    test_url = "https://movie.naver.com/movie/bi/mi/basic.nhn?code=185293"
    title, image, desc = get_movie_info(test_url)

    assert title == "내일의 기억"
    assert image == "https://movie-phinf.pstatic.net/20210406_131/1617688160755B157W_JPEG/movie_image.jpg?type=m665_443_2"
    assert desc == """사고로 기억을 잃은 채 깨어난 수진 옆엔자상한 남편 지훈이 그녀를 세심하게 돌봐주고 있다.그리고 집..."""