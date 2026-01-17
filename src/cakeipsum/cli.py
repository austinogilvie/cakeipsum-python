"""Command-line interface for cakeipsum."""

import argparse
import textwrap
import sys

from .generator import CakeIpsum


def get_version() -> str:
    """Get package version."""
    try:
        from importlib.metadata import version
        return version("cakeipsum")
    except Exception:
        return "0.1.0"


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        prog="cakeipsum",
        description="Generate cake/dessert-themed Lorem Ipsum text.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""
            Examples:
              cakeipsum                         # 1 medium paragraph
              cakeipsum -p 3                    # 3 medium paragraphs
              cakeipsum -w 20                   # 20 words
              cakeipsum -s 5                    # 5 sentences
              cakeipsum -p 2 --long             # 2 long paragraphs
              cakeipsum --start-with-cake-ipsum # Start with "Cake ipsum dolor sit amet"
              cakeipsum --love                  # Include "I love" phrases
        """),
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {get_version()}",
    )

    # Output type (mutually exclusive)
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument(
        "-w", "--words",
        type=int,
        metavar="N",
        help="Output N words",
    )
    output_group.add_argument(
        "-s", "--sentences",
        type=int,
        metavar="S",
        help="Output S sentences",
    )
    output_group.add_argument(
        "-p", "--paragraphs",
        type=int,
        metavar="P",
        default=None,
        help="Output P paragraphs (default: 1)",
    )

    # Paragraph length (mutually exclusive)
    length_group = parser.add_mutually_exclusive_group()
    length_group.add_argument(
        "--short",
        action="store_const",
        const="short",
        dest="length",
        help="Short paragraphs (3-5 sentences)",
    )
    length_group.add_argument(
        "--medium",
        action="store_const",
        const="medium",
        dest="length",
        help="Medium paragraphs (6-11 sentences, default)",
    )
    length_group.add_argument(
        "--long",
        action="store_const",
        const="long",
        dest="length",
        help="Long paragraphs (12-15 sentences)",
    )

    # Options
    parser.add_argument(
        "--love",
        action="store_true",
        help="Include 'I love' phrases (10%% chance)",
    )
    parser.add_argument(
        "--start-with-cake-ipsum",
        action="store_true",
        help="Start text with 'Cake ipsum dolor sit amet'",
    )
    parser.add_argument(
        "--cols",
        type=int,
        default=80,
        metavar="COLS",
        help="Line width for wrapping (default: 80, 0 for no wrap)",
    )

    return parser


def wrap_text(text: str, width: int) -> str:
    """Wrap text to specified width, preserving paragraph breaks."""
    if width <= 0:
        return text

    paragraphs = text.split("\n\n")
    wrapped_paragraphs = []

    for para in paragraphs:
        wrapped = textwrap.fill(para, width=width)
        wrapped_paragraphs.append(wrapped)

    return "\n\n".join(wrapped_paragraphs)


def main(argv: list = None) -> int:
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args(argv)

    # Create generator with options
    generator = CakeIpsum(
        start_with_cake_ipsum=args.start_with_cake_ipsum,
        love=args.love,
    )

    # Determine output type and generate text
    if args.words is not None:
        if args.words <= 0:
            print("Error: Number of words must be positive", file=sys.stderr)
            return 1
        text = generator.words(args.words)
    elif args.sentences is not None:
        if args.sentences <= 0:
            print("Error: Number of sentences must be positive", file=sys.stderr)
            return 1
        text = generator.sentences(args.sentences)
    else:
        # Default to paragraphs
        count = args.paragraphs if args.paragraphs is not None else 1
        if count <= 0:
            print("Error: Number of paragraphs must be positive", file=sys.stderr)
            return 1
        length = args.length if args.length else "medium"
        text = generator.paragraphs(count, length=length)

    # Wrap and output
    output = wrap_text(text, args.cols)
    print(output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
