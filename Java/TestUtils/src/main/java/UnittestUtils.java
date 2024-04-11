
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class UnittestUtils {

//	private static UnittestUtils my = new UnittestUtils();
	private static Logger log = LoggerFactory.getLogger(UnittestUtils.class);
	
	
	/**
	 * 作業用のWorkフォルダを作成し、終了後に削除する
	 * @param prefix Workフォルダのprefix
	 * @return 作成したWorkフォルダのパス
	 * @throws IOException
	 */
	static Path createTempDirectory(final String prefix) throws IOException {
		log.debug("START({})", prefix);
		var path = Files.createTempDirectory(prefix);
		path.toFile().deleteOnExit();
		log.debug("END({})", path);
		return path;
	}
	
	/**
	 * 作業用のWorkファイルを作成し、終了後に削除する
	 * @param dir Workファイルを作成するフォルダ
	 * @param prefix Workファイルのprefix
	 * @return 作成したWorkファイルのパス
	 * @throws IOException
	 */
	static Path createTempfile(final Path dir, final String prefix) throws IOException {
		log.debug("START({}, {})",dir, prefix);
		var path = Files.createTempFile(dir, prefix, "");
		path.toFile().deleteOnExit();
		log.debug("END({})", path);
		return path;
	}
	
	/**
	 * テキストファイルを作成し、終了後に削除する
	 * @param dir ファイルを作成するフォルダ
	 * @param filename 作成するファイル名
	 * @param content テキストデータ
	 * @return 作成したファイルのパス
	 * @throws IOException
	 */
	static Path createFile(final Path dir, final String filename, final String content) throws IOException {
		log.debug("START({}, {}, {})",dir, filename, content);
		if (Files.exists(dir)){
			log.debug("Directory({}) is exist.", dir);
		}else {
			log.debug("Directory({}) is not exist. Create.", dir);
			Files.createDirectories(dir);
			dir.toFile().deleteOnExit();
		}
		var path = Files.writeString(dir.resolve(filename), content);
		path.toFile().deleteOnExit();
		log.debug("END({})", path);
		return path;
	}
	
	static Path getResourceFilePath(final String filename) throws IOException {
		log.debug("START({})",filename);
		try {
//			var path = Paths.get(new URI(my.getClass().getResource(filename).toString()));
			URL url = UnittestUtils.class.getResource(filename);
			var path = Paths.get(new URI(url.toString()));
			log.debug("END({})", path);
			return path;
		} catch (NullPointerException | URISyntaxException e) {
			throw new IOException(String.format("file(%s) is %s Error!", filename, e.toString()), e);
		}
	}
	
	static Path copy(final String resource, final Path dest) throws IOException {
		log.debug("1START({}, {})",resource, dest);
		var resourcepath = getResourceFilePath(resource);
		var path = Files.copy(resourcepath, dest.resolve(resource));
		path.toFile().deleteOnExit();
		log.debug("END({})", path);
		return path;
	}
	
}
