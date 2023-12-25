

import static org.assertj.core.api.Assertions.*;

import java.io.IOException;
import java.nio.file.Path;

import org.junit.jupiter.api.Test;

public class TestUnittestUtils {

	@Test
	void test_createFile() throws IOException {
		Path dir = UnittestUtils.createTempDirectory("prefix");
		Path result =UnittestUtils.createFile(dir.resolve("aaa\\bbb"), "test1.txt", "ABC");
		assertThat(result).isNotNull();
	}
}
