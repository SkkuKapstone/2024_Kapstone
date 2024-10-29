/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}", // src 폴더 내의 모든 JSX/TSX 파일을 대상으로 Tailwind CSS를 적용
  ],
  theme: {
    extend: {
      colors: {
        skkuGreen: "#0E341B", // 커스텀 색상 추가
      },
      fontFamily: {
        sans: ["Roboto", "sans-serif"], // 기본 폰트를 Roboto로 설정
      },
    },
  },
  plugins: [],
};
