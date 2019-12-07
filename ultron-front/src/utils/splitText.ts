interface IProps {
  text: string;
  separator?: string;
  count?: number;
}

export default ({ text, separator = '', count = 2 }: IProps) => {
  const splittedText = text.split(separator);
  const leftSide: string[] = [];
  const rest: string[] = [];

  splittedText.forEach((letter, idx) => {
    if (idx < count) {
      leftSide.push(letter);
    } else {
      rest.push(letter);
    };
  });

  return [leftSide.join(''), rest.join('')];
};
