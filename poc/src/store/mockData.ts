export interface Book {
  id: string
  title: string
  author: string
  publisher: string
  year: number
  category: string
  tags: string[]
  access: 'Public' | 'Internal' | 'Restricted'
  cover: string
  description: string
  pages: number
  ocrAccuracy: number
  content: string // HTML content for the reader
}

export const CATEGORIES = [
  'Khoa học Máy tính',
  'Toán học',
  'Vật lý',
  'Hóa học',
  'Sinh học',
  'Kinh tế',
  'Ngôn ngữ học',
  'Lịch sử & Văn hóa',
]

export const mockBooks: Book[] = [
  {
    id: 'b001',
    title: 'Cấu trúc Dữ liệu và Giải thuật',
    author: 'Nguyễn Văn An',
    publisher: 'NXB ĐHQG-HCM',
    year: 2022,
    category: 'Khoa học Máy tính',
    tags: ['#GiaoTrinh', '#CTDL', '#Algorithm', '#CS101'],
    access: 'Internal',
    cover: '🖥️',
    description: 'Giáo trình cơ bản về cấu trúc dữ liệu: mảng, danh sách liên kết, cây nhị phân, đồ thị và các giải thuật sắp xếp, tìm kiếm nền tảng.',
    pages: 324,
    ocrAccuracy: 94.2,
    content: `
      <h1>Chương 2: Các Giải thuật Tìm kiếm</h1>
      <p>Trong chương này, chúng ta sẽ khảo sát các giải thuật tìm kiếm cơ bản và nâng cao, phân tích độ phức tạp thời gian và không gian của từng giải thuật.</p>
      <h2>2.1. Tìm kiếm Tuyến tính (Linear Search)</h2>
      <p>Tìm kiếm tuyến tính là giải thuật đơn giản nhất. Ý tưởng cơ bản: duyệt qua tất cả các phần tử trong danh sách từ đầu đến cuối cho đến khi tìm thấy phần tử cần tìm hoặc đã duyệt hết danh sách.</p>
      <pre><code>def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Trả về chỉ số tìm thấy
    return -1  # Không tìm thấy</code></pre>
      <p><strong>Độ phức tạp:</strong> O(n) trong trường hợp xấu nhất.</p>
      <h2>2.2. Tìm kiếm Nhị phân (Binary Search)</h2>
      <p>Tìm kiếm nhị phân hiệu quả hơn nhiều nhưng yêu cầu danh sách phải được sắp xếp trước. Giải thuật chia đôi không gian tìm kiếm trong mỗi bước.</p>
      <pre><code>def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1</code></pre>
      <p><strong>Độ phức tạp:</strong> O(log n) — hiệu quả hơn tuyến tính rất nhiều với dữ liệu lớn.</p>
      <h2>2.3. So sánh các Giải thuật Tìm kiếm</h2>
      <table>
        <tr><th>Giải thuật</th><th>Trường hợp tốt nhất</th><th>Trường hợp xấu nhất</th><th>Yêu cầu</th></tr>
        <tr><td>Linear Search</td><td>O(1)</td><td>O(n)</td><td>Không cần sắp xếp</td></tr>
        <tr><td>Binary Search</td><td>O(1)</td><td>O(log n)</td><td>Phải sắp xếp trước</td></tr>
        <tr><td>Hash Search</td><td>O(1)</td><td>O(n)</td><td>Cần bảng băm</td></tr>
      </table>
    `,
  },
  {
    id: 'b002',
    title: 'Giải tích 1 — Hàm một biến',
    author: 'Trần Thị Bình',
    publisher: 'NXB Giáo dục Việt Nam',
    year: 2021,
    category: 'Toán học',
    tags: ['#GiaoTrinh', '#Calculus', '#Math', '#Limit'],
    access: 'Public',
    cover: '📐',
    description: 'Giáo trình giải tích hàm một biến bao gồm giới hạn, đạo hàm, tích phân và ứng dụng trong kỹ thuật và khoa học tự nhiên.',
    pages: 412,
    ocrAccuracy: 91.5,
    content: `
      <h1>Chương 3: Đạo Hàm và Vi Phân</h1>
      <p>Đạo hàm là một trong những khái niệm trung tâm của giải tích, mô tả tốc độ thay đổi của hàm số tại một điểm.</p>
      <h2>3.1. Định nghĩa Đạo hàm</h2>
      <p>Cho hàm số f(x) xác định trên khoảng (a, b). Đạo hàm của f tại điểm x₀ ∈ (a, b) được định nghĩa là:</p>
      <blockquote>f'(x₀) = lim[Δx→0] (f(x₀ + Δx) - f(x₀)) / Δx</blockquote>
      <p>nếu giới hạn này tồn tại và hữu hạn.</p>
      <h2>3.2. Các Quy tắc Tính Đạo hàm</h2>
      <ul>
        <li><strong>Quy tắc tổng:</strong> (f + g)' = f' + g'</li>
        <li><strong>Quy tắc tích:</strong> (fg)' = f'g + fg'</li>
        <li><strong>Quy tắc thương:</strong> (f/g)' = (f'g - fg') / g²</li>
        <li><strong>Quy tắc hàm hợp:</strong> (f∘g)'(x) = f'(g(x)) · g'(x)</li>
      </ul>
    `,
  },
  {
    id: 'b003',
    title: 'Lập trình Hướng đối tượng với Java',
    author: 'Lê Minh Cường',
    publisher: 'NXB Thông tin và Truyền thông',
    year: 2023,
    category: 'Khoa học Máy tính',
    tags: ['#GiaoTrinh', '#Java', '#OOP', '#Programming'],
    access: 'Internal',
    cover: '☕',
    description: 'Giáo trình lập trình hướng đối tượng với Java từ cơ bản đến nâng cao: class, inheritance, polymorphism, interface, exception handling và Java Collections.',
    pages: 520,
    ocrAccuracy: 96.8,
    content: `
      <h1>Chương 5: Kế thừa và Đa hình</h1>
      <p>Kế thừa (Inheritance) là một trong bốn trụ cột của lập trình hướng đối tượng, cho phép một lớp con kế thừa các thuộc tính và phương thức từ lớp cha.</p>
      <h2>5.1. Kế thừa đơn (Single Inheritance)</h2>
      <pre><code>public class Animal {
    protected String name;
    protected int age;
    
    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public void speak() {
        System.out.println("...");
    }
}

public class Dog extends Animal {
    private String breed;
    
    public Dog(String name, int age, String breed) {
        super(name, age); // Gọi constructor lớp cha
        this.breed = breed;
    }
    
    @Override
    public void speak() {
        System.out.println(name + " nói: Gâu gâu!");
    }
}</code></pre>
      <h2>5.2. Đa hình (Polymorphism)</h2>
      <p>Đa hình cho phép các đối tượng thuộc các lớp khác nhau được xử lý thông qua một giao diện chung.</p>
    `,
  },
  {
    id: 'b004',
    title: 'Vật lý Đại cương — Cơ học và Nhiệt học',
    author: 'Phạm Quốc Dũng',
    publisher: 'NXB ĐHQG-HCM',
    year: 2020,
    category: 'Vật lý',
    tags: ['#GiaoTrinh', '#Physics', '#Mechanics', '#Thermodynamics'],
    access: 'Public',
    cover: '⚛️',
    description: 'Vật lý đại cương phần Cơ học và Nhiệt học: định luật Newton, năng lượng, dao động, sóng cơ, nhiệt động lực học và các nguyên lý cơ bản.',
    pages: 380,
    ocrAccuracy: 88.3,
    content: `
      <h1>Chương 4: Định luật Bảo toàn Năng lượng</h1>
      <p>Định luật bảo toàn năng lượng là một trong những định luật cơ bản nhất của vật lý. Năng lượng không tự sinh ra và không tự mất đi, nó chỉ chuyển hóa từ dạng này sang dạng khác.</p>
      <h2>4.1. Công và Năng lượng</h2>
      <p>Công (W) được thực hiện khi lực F tác dụng làm vật dịch chuyển một đoạn d:</p>
      <blockquote>W = F · d · cos(θ)</blockquote>
      <p>trong đó θ là góc giữa lực và hướng dịch chuyển.</p>
      <h2>4.2. Động năng và Thế năng</h2>
      <ul>
        <li><strong>Động năng:</strong> Eₖ = ½mv²</li>
        <li><strong>Thế năng trọng trường:</strong> Eₚ = mgh</li>
        <li><strong>Cơ năng toàn phần:</strong> E = Eₖ + Eₚ = const (khi không có lực ma sát)</li>
      </ul>
    `,
  },
  {
    id: 'b005',
    title: 'Kinh tế Vi mô — Nguyên lý cơ bản',
    author: 'Hoàng Thị Lan',
    publisher: 'NXB Kinh tế TP.HCM',
    year: 2022,
    category: 'Kinh tế',
    tags: ['#GiaoTrinh', '#Economics', '#Microeconomics', '#Market'],
    access: 'Internal',
    cover: '📊',
    description: 'Giáo trình kinh tế vi mô bao gồm lý thuyết người tiêu dùng, lý thuyết hãng, cấu trúc thị trường và phân tích cân bằng cung cầu.',
    pages: 456,
    ocrAccuracy: 92.7,
    content: `
      <h1>Chương 3: Lý thuyết Cung và Cầu</h1>
      <p>Cung và cầu là hai lực lượng cơ bản quyết định giá cả và sản lượng trên thị trường. Sự cân bằng giữa cung và cầu xác định điểm cân bằng thị trường.</p>
      <h2>3.1. Đường Cầu (Demand Curve)</h2>
      <p>Đường cầu mô tả mối quan hệ nghịch chiều giữa giá cả và lượng cầu. Khi giá tăng, lượng cầu giảm và ngược lại (giữ nguyên các yếu tố khác).</p>
      <blockquote>Qd = a - bP (a, b > 0)</blockquote>
      <h2>3.2. Đường Cung (Supply Curve)</h2>
      <p>Đường cung mô tả mối quan hệ thuận chiều giữa giá cả và lượng cung. Khi giá tăng, nhà sản xuất sẵn sàng cung cấp nhiều hàng hóa hơn.</p>
      <blockquote>Qs = c + dP (c có thể âm, d > 0)</blockquote>
    `,
  },
]

export function searchBooks(query: string, category: string): Book[] {
  const q = query.toLowerCase().trim()
  return mockBooks.filter(book => {
    const matchCategory = !category || book.category === category
    if (!q) return matchCategory
    const matchText =
      book.title.toLowerCase().includes(q) ||
      book.author.toLowerCase().includes(q) ||
      book.description.toLowerCase().includes(q) ||
      book.tags.some(t => t.toLowerCase().includes(q)) ||
      book.content.toLowerCase().includes(q)
    return matchCategory && matchText
  })
}
