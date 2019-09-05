import GetFramesStream
import click

@click.command()
@click.argument('input')
@click.argument('fps')

def main(input, fps):
  f = GetFramesStream.GetFramesStream("data/images/")
  f.extract_frames(input, fps)

if __name__ == '__main__':
  main()