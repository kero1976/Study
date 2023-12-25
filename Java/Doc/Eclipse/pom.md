# 1.標準設定
## 1-1.Java Version指定

```
	<build>
		<plugins>
			<!-- コンパイル設定 -->
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-compiler-plugin</artifactId>
				<version>3.10.1</version>
				<configuration>
					<release>11</release>
				</configuration>
			</plugin>
		</plugins>
	</build>
```

# 2.追加ライブラリ

## 2-1.logger

```
		<dependency>
			<groupId>ch.qos.logback</groupId>
			<artifactId>logback-classic</artifactId>
			<version>1.2.11</version>
		</dependency>

		<dependency>
			<groupId>ch.qos.logback</groupId>
			<artifactId>logback-core</artifactId>
			<version>1.2.11</version>
		</dependency>
```